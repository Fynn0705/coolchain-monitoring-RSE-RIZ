from datenbank import hole_daten
from pruefung_stimmigkeit import pruefe_stimmigkeit
from pruefung_pause import pruefe_pause
from pruefung_dauer import pruefe_dauer

def pruefe_transport(transport_id):
    daten = hole_daten(transport_id)
    ok1, m1 = pruefe_stimmigkeit(daten)
    ok2, m2 = pruefe_pause(daten)
    ok3, m3 = pruefe_dauer(daten)
    gesamt_ok = ok1 and ok2 and ok3
    return gesamt_ok, [m1, m2, m3]

if __name__ == "__main__":
    test_id = "72359278599178561029675"
    ok, meldungen = pruefe_transport(test_id)
    print("Ergebnis:", "OK" if ok else "FEHLER")
    for m in meldungen:
        print("-", m)
