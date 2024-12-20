<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommender</title>
</head>
<body>
    <h1>Recomendador de Películas</h1>
    <form id="recommend-form">
        <label for="movie">Ingresa el título de una película:</label><br>
        <input type="text" id="movie" name="movie" required><br><br>
        <button type="submit">Recomendar</button>
    </form>
    <h2>Recomendaciones:</h2>
    <ul id="recommendations"></ul>
    <script>
        document.getElementById('recommend-form').onsubmit = async function(event) {
            event.preventDefault();
            const movie = document.getElementById('movie').value;
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `movie=${encodeURIComponent(movie)}`
            });
            const data = await response.json();
            const recommendationsList = document.getElementById('recommendations');
            recommendationsList.innerHTML = '';
            if (data.error) {
                recommendationsList.innerHTML = `<li>${data.error}</li>`;
            } else {
                data.recommendations.forEach(rec => {
                    recommendationsList.innerHTML += `<li>${rec}</li>`;
                });
            }
        };
    </script>
</body>
</html>
