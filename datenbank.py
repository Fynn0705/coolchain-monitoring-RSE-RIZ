import pyodbc

def hole_daten(transport_id):
    # Verbindung zur Datenbank
    verbindung = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"  # falls du nur den 18er hast: 17 -> 18
        "SERVER=sc-db-server.database.windows.net;"
        "DATABASE=supplychain;"
        "UID=rse;"
        "PWD=Pa$$w0rd"
    )
    cursor = verbindung.cursor()

    # Daten für eine Transport-ID abfragen (einfach gehalten)
    cursor.execute(
        f"SELECT * FROM dbo.coolchain WHERE transportid = '{transport_id}' ORDER BY datetime"
    )
    daten = cursor.fetchall()

    cursor.close()
    verbindung.close()
    return daten

# Schnelltest direkt ausführen:
if __name__ == "__main__":
    test_id = "72359278599178561029675"
    for zeile in hole_daten(test_id):
        print(zeile)
