from omdbapi.movie_search import GetMovie
import psycopg2

try:
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="2171985",
        host="localhost",
        port="5432"
    )

    if connection:
        print("Σύνδεση στη βάση δεδομένων πραγματοποιήθηκε επιτυχώς.")

    api_key = 'c862ab2f'  # Αντικαταστήστε με το πραγματικό σας κλειδί πρόσβασης
    movie = GetMovie(api_key=api_key)

    results = []

    while True:

        # Ζητήστε από τον χρήστη το όνομα της ταινίας
        movie_name = input("Give a Movie Name For Details (or press Enter for exit ): ")

        if not movie_name:
            break

        # Αναζήτηση των πληροφοριών της ταινίας
        result = movie.get_movie(title=movie_name)

        if not result:
            print("No Movie Result.")

        else:
            results.append(result)
            print(result)

            cursor = connection.cursor()

            create_table_query = "CREATE TABLE IF NOT EXISTS movies (title VARCHAR(255))"
            cursor.execute(create_table_query)

            insert_query = "INSERT INTO movies (title) VALUES (%s)"
            data = (result['title'],)  # Χρησιμοποιήστε το ονομαστικό όνομα του πεδίου "title" στο αντικείμενο result.
            cursor.execute(insert_query, data)
            connection.commit()
            cursor.close()

except Exception as e:
    print(f"Error: {e}")

connection.close()
