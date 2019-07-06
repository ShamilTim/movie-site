INSERT INTO feature_films(id, title, release_year, country, director, main_roles, genres, box_office, brief_description,
                          certificate, runtime, tags) VALUES
(
 'cbad028d-2180-4e9d-b217-17d2c26a79e1',
 'The Shawshank Redemption',
 1994,
 'USA',
 'Frank Darabont',
 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown, Gil Bellows, Mark Rolston, James Whitmore',
 'Drama',
 59840000,
 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
 '16+',
 '2:22',
 'freedom, hope, prison, escape, system'
 ),
(
 '4b0d6d45-b489-4521-bf6c-a25b529fa2ad',
 'The Green Mile',
 1999,
 'USA',
 'Frank Darabont',
 'Tom Hanks, David Morse, Bonnie Hunt, Michael Clarke Duncan, James Cromwell, Michael Jeter, Graham Greene',
 'Crime, Drama, Fantasy, Mystery',
 286801000,
 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.',
 '16+',
 '3:09',
 'good, hope, miracle, prison, struggle'
 ),
(
 '99a96677-7e62-4d1d-91e4-841312945061',
 'Forrest Gump',
 '1994',
 'USA',
 'Robert Zemeckis',
 'Tom Hanks, Rebecca Williams, Sally Field, Michael Conner Humphreys, Harold G. Herthum, George Kelly, Bob Penny',
 'Drama, Romance',
 677386686,
 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.',
 '12+',
 '2:22',
 'development, kind, military, naive, president, service'
 );

INSERT INTO documentary_films(id, title, release_year, country, director, category, brief_description, certificate, runtime, tags) VALUES
(
 'f8ccc193-e136-4e5b-a95e-5f887ff02df9',
 'The Brain with Dr. David Eagleman',
 2015,
 'USA',
 'Glenn Barden',
 'Research',
 'Six one-hour episodes that tell the story of the inner workings of the brain and take viewers on a visually spectacular journey into why they feel and think the things they do.',
 '12+',
 '6 episodes for 1 hour',
 'science, brain, reflexes, consciousness, mind'
),
(
 'fed1c34a-71a6-497f-b4cc-2ad0c443df95',
 'Apollo 11',
 2019,
 'USA',
 'Todd Douglas Miller',
 'Chronicle',
 'A look at the Apollo 11 mission to land on the moon led by commander Neil Armstrong and pilots Buzz Aldrin and Michael Collins.',
 '0+',
 '1:23',
 'space, Neil Armstrong, Moon, mission, Earth'
),
(
 'd4991c9b-c759-485c-8253-cb14c3a99a0d',
 'Meeting Gorbachev',
 2018,
 'USA',
 'Werner Herzog',
 'Chronicle, Propaganda(history)',
 'The life of Mikhail Gorbachev, the eighth and final President of the Soviet Union in chronological order.',
 '12+',
 '01:30',
 'history, USSR, breakup, cold war, GDR(German Democratic Republic)'
);

INSERT INTO cartoons(id, title, release_year, country, method_of_creation, director, genres, brief_description,
                 certificate, duration, runtime, tags) VALUES
(
 '9c004bcb-5e7b-48d3-9fb8-39f3261f0941',
 'The Secret Life of Pets',
 2016,
 'Japan, USA, France',
 'CGI-animation',
 'Chris Renaud',
 'adventure, comedy, family',
 'The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.',
 '6+',
 'full-length',
 '01:27',
 'pets, relationship, dogs, homecoming, secret life'
),
(
 'e50c366c-9da7-42b6-a537-f44efcc634d2',
 '5 centimeters per second',
 2007,
 'Japan',
 'painted',
 'Makoto Shinkai',
 'drama, romance',
 'Told in three interconnected segments, we follow a young man named Takaki through his life as cruel winters, cold technology, and finally, adult obligations and responsibility converge to test the delicate petals of love.',
 '12+',
 'short-length',
 '1:03',
 'three stories, romance, Japan, relationship, love'
),
(
 'd0f1f200-a19a-40e4-8c78-54b99332a388',
 'Shaun the Sheep Movie',
 2015,
 'UK, France, USA',
 'plasticine',
 'Mark Burton',
 'adventure, Comedy, family, fantasy',
 'When Shaun decides to take the day off and have some fun, he gets a little more action than he bargained for. A mix up with the Farmer, a caravan and a very steep hill lead them all to the Big City and it''s up to Shaun and the flock to return everyone safely to the green grass of home.',
 '0+',
 'full-length',
 '1:21',
 'sheep, dogs, farm, mutual assistance, rescue'
)