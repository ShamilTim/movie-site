INSERT INTO feature_films(title, release_year, country, director, main_roles, genres, box_office, brief_description,
                          certificate, runtime, tags) VALUES
(
 'The Shawshank Redemption',
 1994,
 'USA',
 'Frank Darabont',
 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown, Gil Bellows, Mark Rolston, James Whitmore',
 'Drama',
 59840000,
 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
 16,
 '2:22',
 'freedom, hope, prison, escape, system'
 ),
(
 'The Green Mile',
 1999,
 'USA',
 'Frank Darabont',
 'Tom Hanks, David Morse, Bonnie Hunt, Michael Clarke Duncan, James Cromwell, Michael Jeter, Graham Greene',
 'Crime, Drama, Fantasy, Mystery',
 286801000,
 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.',
 16,
 '3:09',
 'good, hope, miracle, prison, struggle'
 ),
(
 'Forrest Gump',
 '1994',
 'USA',
 'Robert Zemeckis',
 'Tom Hanks, Rebecca Williams, Sally Field, Michael Conner Humphreys, Harold G. Herthum, George Kelly, Bob Penny',
 'Drama, Romance',
 677386686,
 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.',
 12,
 '2:22',
 'development, kind, military, naive, president, service'
 );

INSERT INTO documentary_films(title, release_year, country, director, category, brief_description, certificate, runtime, tags) VALUES
(
 'The Brain with Dr. David Eagleman',
 2015,
 'USA',
 'Glenn Barden',
 'Research',
 'Six one-hour episodes that tell the story of the inner workings of the brain and take viewers on a visually spectacular journey into why they feel and think the things they do.',
 12,
 '6 episodes for 1 hour',
 'science, brain, reflexes, consciousness, mind'
),
(
 'Apollo 11',
 2019,
 'USA',
 'Todd Douglas Miller',
 'Chronicle',
 'A look at the Apollo 11 mission to land on the moon led by commander Neil Armstrong and pilots Buzz Aldrin and Michael Collins.',
 0,
 '1:23',
 'space, Neil Armstrong, Moon, mission, Earth'
),
(
 'Meeting Gorbachev',
 2018,
 'USA',
 'Werner Herzog',
 'Chronicle, Propaganda(history)',
 'The life of Mikhail Gorbachev, the eighth and final President of the Soviet Union in chronological order.',
 12,
 '01:30',
 'history, USSR, breakup, cold war, GDR(German Democratic Republic)'
);

INSERT INTO cartoons(title, release_year, country, method_of_creation, director, genres, brief_description,
                 certificate, duration, runtime, tags) VALUES
(
 'The Secret Life of Pets',
 2016,
 'Japan, USA, France',
 'CGI-animation',
 'Chris Renaud',
 'adventure, comedy, family',
 'The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.',
 6,
 'full-length',
 '01:27',
 'pets, relationship, dogs, homecoming, secret life'
),
(
'5 centimeters per second',
 2007,
 'Japan',
 'painted',
 'Makoto Shinkai',
 'drama, romance',
 'Told in three interconnected segments, we follow a young man named Takaki through his life as cruel winters, cold technology, and finally, adult obligations and responsibility converge to test the delicate petals of love.',
 12,
 'short-length',
 '1:03',
 'three stories, romance, Japan, relationship, love'
),
(
 'Shaun the Sheep Movie',
 2015,
 'UK, France, USA',
 'plasticine',
 'Mark Burton',
 'adventure, Comedy, family, fantasy',
 'When Shaun decides to take the day off and have some fun, he gets a little more action than he bargained for. A mix up with the Farmer, a caravan and a very steep hill lead them all to the Big City and it''s up to Shaun and the flock to return everyone safely to the green grass of home.',
 0,
 'full-length',
 '1:21',
 'sheep, dogs, farm, mutual assistance, rescue'
)