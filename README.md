
# Shark Art-tack

Ancient creatures roam through the depths and breadths of ocean basins. Their size, their jaws, their might, and their electroreceptive abilities are some of the qualities that inspire both awe and fear of these apex predators. But how do sharks go about in their predation?

In contrast to cultural depictions of the lone hunter, many shark species [hunt collectively](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecy.3117). Ecologist Mourier argues this feeding pattern is a demonstration of how "sharks can use collective behavior with simple rules to benefit and increase their [fitness](https://www.psychologytoday.com/ca/blog/animal-minds/202006/the-sharks-hunt-in-packs#:~:text=It%20is%20the%20hunting%20grounds,The%20sharks%20hunt%20in%20packs.)". 

Our objective, then, was to simulate sharks gathering around a feeding ground in order to assess potentially relevant parameters governing these 'simple rules' in collective hunting. 


## The Model 

The simulation of collective hunting takes into account the following parameters: velocity of shark, position of shark, hunger level, which in turn influences proximity to food source, and repulsion from other sharks. 

How it works:
We adopted a simplified 3D swarming model defined by [Couzin et. al](https://pubmed.ncbi.nlm.nih.gov/12297066/) and modified it to take feeding into account.
The position ($r_i(t)$) and direction ($v_i(t)$) of each shark at every time-step $\tau$ changes according to a set of rules. 
In general:
\begin{align}
  v_i(t + \tau) &= v_i(t) + a_i(t)\tau \\
  r_i(t + \tau) &= r_i(t) + v_i(t)\tau
  \label{eq:eom}
\end{align}
where $a_i(t)$ is a measure for the net interaction of one shark with all the others and the feeding point.

Modeling shark-shark interactions:
For every shark ($r_s$, $v_s$), three zones of interaction are identified (from smallest to largest): 
\begin{enumerate}
  \item zone of repulsion (zor): A number of $N_r$ sharks inside this zone contribute to $a_i$ by a repulsive component
    \begin{equation}
      a_r = -\sum_{j = 0}^{N_r}\frac{r_j - r_s}{|r_j - r_s|^n}.
      \label{eq:zor}
    \end{equation}
    This simulates the size of each shark. The exponent $n$ is a parameter that we let vary.
  \item zone of orientation (zoo): A number of $N_o$ sharks inside this zone contribute to $a_i$ by tending to align neighbouring sharks:
    \begin{equation}
      a_o = \frac{1}{\tau}\sum_{j=0}^{N_o}v_j.
      \label{eq:zoo}
    \end{equation}
    A shark tends to align it's direction according to it's nearest neighbours inside this zone.
  \item zone of attraction (zoa): Outside the zoo, sharks are generally drawn towards each other using an attractive force
    \begin{equation}
      a_a = \sum_{j=0}^{N_a} \frac{r_j - r_s}{|r_j - r_s|^m}.
      \label{eq:zoa}
    \end{equation}
    Sharks that are separated far from each other tend to be attract.
\end{enumerate}


## The Visualization

Art moves the soul . In this visualization, the collective movement of sharks in turn produces a simple yet mesmerizing pattern of dynamic interactions, balanced between attraction towards the food source and repulsion in space from others, to yield a state in which nourishment of the soul is achieved, both of the sharks, and of the perceiver of this beautiful simulation. 
