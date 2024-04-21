#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
	} else if (response.statusCode !== 200) {
		console.error('Status:', response.statusCode);
	} else {
		const film = JSON.parse(body)
		const characterUrls = film.characters;

		const promises = characterUrls.map(characterUrl => {
			return new Promise((resolve, reject) => {
				request(characterUrl, (error, response, body) => {
					if (error) {
						reject(error);
					} else if (response.statusCode !== 200) {
						reject(`Failed to fetch character data for ${chracterUrl}`);
					} else {
						const character = JSON.parse(body);
						resolve(character.name);
					}
				});
			});
		});

		Promise.all(promises)
			.then(characterNames => {
				characterNames.forEach(name => console.log(name));
			})
			.catch(error => {
				console.error('Error:', error);
			});
	}
});
