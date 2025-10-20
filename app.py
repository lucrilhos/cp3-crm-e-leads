from stages import Lead
import repo

def add_flow():
    name = input("Nome: ").strip()
    company = input("Empresa: ").strip()
    email = input("E-mail: ").strip()
    if not name or not email or "@" not in email:
        print("É necessário um nome e um e-mail válidos.")
        return

    lead = Lead(name, company, email)
    print(lead.to_dict())
    repo.add_lead(lead)
    print("Lead adicionada")

def list_flow():
    leads = repo.list_leads()
    if not leads:
        print("Nenhuma lead ainda")
        return
    print("\n# | Nome                 | Empresa            | E-mail")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in enumerate(leads):
        # trata caso l seja um dict ou um objeto Lead (segurança extra)
        name = l.name if hasattr(l, "name") else l.get("name", "")
        company = l.company if hasattr(l, "company") else l.get("company", "")
        email = l.email if hasattr(l, "email") else l.get("email", "")
        print(f"{i:02d}| {name:<20} | {company:<17} | {email:<21}")

def search_flow():
    q = input("Buscar por: ").strip().lower()
    if not q:
        print("Consulta vazia")
        return
    leads = repo.list_leads()
    results = []
    for i, l in enumerate(leads):
        name = l.name if hasattr(l, "name") else l.get("name", "")
        company = l.company if hasattr(l, "company") else l.get("company", "")
        email = l.email if hasattr(l, "email") else l.get("email", "")
        blob = f"{name} {company} {email}".lower()
        if q in blob:
            results.append((i, l))
    if not results:
        print("Nada encontrado.")
        return
    print("\n# | Nome                 | Empresa            | E-mail")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in results:
        name = l.name if hasattr(l, "name") else l.get("name", "")
        company = l.company if hasattr(l, "company") else l.get("company", "")
        email = l.email if hasattr(l, "email") else l.get("email", "")
        print(f"{i:02d}| {name:<20} | {company:<17} | {email:<21}")

def export_flow():
    path = repo.export_csv()
    if path is None:
        print("Não consegui escrever o CSV. feche o arquivo se estiver aberto ou tente novamente")
    else:
        print(f"✔ Exportado para: {path}")

def print_menu():
    print("\nMini CRM de Leads — Aula 2 (Adicionar/Listar/Buscar/CSV)")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[3] Buscar (nome/empresa/e-mail)")
    print("[4] Exportar CSV")
    print("[0] Sair")

def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            add_flow()
        elif op == "2":
            list_flow()
        elif op == "3":
            search_flow()
        elif op == "4":
            export_flow()
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
