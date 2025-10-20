from pathlib import Path
from datetime import date
import json, csv
from stages import Lead

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def _normalize_record(r):
    # aceita dicionário parcial; ignora tipos inesperados
    if not isinstance(r, dict):
        return None
    name = r.get("name", "") or ""
    company = r.get("company", "") or ""
    email = r.get("email", "") or ""
    stage = r.get("stage", "novo") or "novo"
    created = r.get("created", date.today().isoformat()) or date.today().isoformat()
    return {"name": name, "company": company, "email": email, "stage": stage, "created": created}

def _load():
    if not DB_PATH.exists():
        return []
    try:
        raw = json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    if not isinstance(raw, list):
        return []

    leads = []
    for item in raw:
        rec = _normalize_record(item)
        if rec is None:
            # pula entradas inválidas que sejam listas, strings, etc.
            continue
        lead = Lead(rec["name"], rec["company"], rec["email"], stage=rec["stage"], created=rec["created"])
        leads.append(lead)
    return leads

def _save(leads):
    raw = [lead.to_dict() for lead in leads]
    DB_PATH.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

def list_leads():
    return _load()

def add_lead(lead_obj):
    leads = _load()
    leads.append(lead_obj)
    _save(leads)

def export_csv(path=None):
    path = Path(path) if path else (DATA_DIR / "leads.csv")
    leads = _load()
    try:
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["name","company","email","stage","created"])
            w.writeheader()
            for lead in leads:
                w.writerow(lead.to_dict())
        return path
    except PermissionError:
        return None
