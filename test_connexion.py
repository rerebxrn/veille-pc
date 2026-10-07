"""Étape 1 : est-ce que Leboncoin répond depuis cet ordinateur / serveur ?"""
import lbc

for navigateur in ["chrome_android", None]:
    try:
        client = lbc.Client(impersonate=navigateur) if navigateur else lbc.Client()
        r = client.search(text="rtx 2060", category=lbc.Category.ELECTRONIQUE_ORDINATEURS,
                          sort=lbc.Sort.NEWEST, limit=5)
        print(f"OK ({navigateur}) : {len(r.ads)} annonces")
        for a in r.ads:
            print(" -", a.subject, "|", a.price, "€ |", getattr(a.location, "city", ""))
        break
    except Exception as e:
        print(f"BLOQUÉ ({navigateur}) : {type(e).__name__} {e}")
