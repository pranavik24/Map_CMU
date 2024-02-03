# Map_CMU
This is our submission to TartanHacks 2024 at Carnegie Mellon Univeristy

## Our Inspiration
We all remember being freshman at Carnegie Mellon, and being overwhelmed by the size of campus and all of the possible tunnels and passageways from building to building. So, we devised an application can can take your daily schedule and suggest the best possible routes to take from class to class. Our application even suggests where the best places to eat are, based on your class locations. 

## Technical Components
The search algorithm used in our application is Uniform-Cost Search, which takes a pixelated-matrix of a CMU map, and then generates an optimal path from your start state to your target. We used the Chebyshev heuristic to find the closest meal location based on the user's current location. 

## Scalability
Currently, we are working on an approximately 150x150 pixel rendering of the map, with limited clarity. In the future, we hope to improve the precision of the building shapes and path, and potentially include floor plans for each building. 

### Note
As the application is hosted on a local host, for personal use, the search function in app.py must be edited to save the rendered images to the absolute path of your local directory. 
