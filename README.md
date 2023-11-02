# Movie-App-OMDB-API--PostgreSQL-

The application you've created connects to a PostgreSQL database and utilizes the OMDB API to fetch movie details. Here's a description of how the application works:

1. It establishes a connection to a PostgreSQL database using the provided database credentials (database name, username, password, host, and port).

2. It prompts the user to input the name of a movie for which they want to retrieve details from the OMDB API.

3. It uses the OMDB API to search for information about the specified movie based on the user's input.

4. If the API returns information about the movie, the application stores the movie's title in a PostgreSQL table called "movies."

5. If there's no result for the movie search, it informs the user that there's no movie result.

6. The application can be used iteratively to fetch and store details of multiple movies into the database.

In summary, the application serves as a movie information retrieval tool. Users can input a movie title, and the application fetches the title and stores it in a PostgreSQL database for future reference. This can be extended to store more movie details beyond just the title by modifying the database schema and the SQL statements accordingly.
