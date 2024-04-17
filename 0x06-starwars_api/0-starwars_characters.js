#!/usr/bin/node

const request = require('request');

function fetchMovieCharacters(movieId) {
	const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

	request(apiUrl, (error, response, body) => {
		if (error) {
			console.error('Error fetching movie information:', error);
			return;
		}

		const movieData = JSON.parse(body);
		const characterUrls = movieData.characters;

		characterUrls.forEach(characterUrl => {
			request(characterUrl, (error, response, body) => {
				if (error) {
					console.error('Error fetching character information:', error);
					return;
				}

				const characterData = JSON.parse(body);
				console.log(characterData.name);
			});
		});
	});
}

const movieId = process.argv[2];
fetchMovieCharacters(movieId);
