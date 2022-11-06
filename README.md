
# Shark Art-tack

Ancient creatures roam through the depths and breadths of ocean basins. Their size, their jaws, their might, and their electroreceptive abilities are some of the qualities that inspire both awe and fear of these apex predators. But how do sharks go about in their predation?

In contrast to cultural depictions of the lone hunter, many shark species [hunt collectively](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecy.3117). Ecologist Mourier argues this feeding pattern is a demonstration of how "sharks can use collective behavior with simple rules to benefit and increase their [fitness](https://www.psychologytoday.com/ca/blog/animal-minds/202006/the-sharks-hunt-in-packs#:~:text=It%20is%20the%20hunting%20grounds,The%20sharks%20hunt%20in%20packs.)". 

Our objective, then, was to simulate sharks gathering around a feeding ground in order to assess potentially relevant parameters governing these 'simple rules' in collective hunting. 


## The Model 

direction, position - influenced by previous timestamp, number of sharks in current time stamp, proximity to food if hungry, velocaity updated at every time stamp (far - swim towards)

a function that will update a class, store values of class into array
output - array of data

model for food - food available at a fixed point randomly, every shark makes decision to get food (exponential of hungry), drawn to source and maintain decision unless food is eaten, grab it and leave it. other sharks maintain hunger that didn't get food and they get closer in proximity to the food source 

## The Visualization

call function