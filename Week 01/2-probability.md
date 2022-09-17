# Probability for Data Science

Probability is measure of likelihood of an event. Some examples of such events are:
* rolling a dice
* tossing a coin
* weather forecast

## Sample Space and Event

The set of all possible outcomes of a statistical experiment is called `sample space`. It is denoted by S. 

Any subset of sample space is called an `event`. For example, S = {H, T}, A={H}, and B={T}. Here, A and B are events and {H, T} are sample points.


## Probability of Event

Probability is always between 0 to 1. For example, the probability of flipping a coin and it being heads is ½, because there is 1 way of getting a head and the total number of possible outcomes is 2. We write P(heads) = ½.


## Mutually Exclusive Events

Mutually exclusive events are those events that **cannot occur at the same time**. For example, when a coin is tossed then the result will be either head or tail, but we cannot get both the results.

If A and B are mutually exclusive events then its probability is given by P(A OR B) or P (A U B). P (A OR B) = P (A ∪ B) = P(A) + P(B) 


## Not Mutually Exclusive Events

Two events are called not mutually exclusive if they have **at least one outcome in common**. If the two events A and B are not mutually exclusive events, then $A ∩ B ≠ ϕ$. Similarly, A, B and C are not mutually exclusive events if $A ∩ B ∩ C ≠ ϕ$.


## Additive Rule

* If A & B are mutually exclusive events: P(A OR B) = P(A) + P(B)
* If A & B are not mutually exclusive events: P(A OR B) = P(A) + P(B) – P(A ∩ B)


## Multiplicative Rule

* If A and B are independent events: P(A AND B)= P(A) $\times$ P(B)
* If A and B are dependent events: P(A AND B) = P(A) $\times$ P(B/A), where P(B/A) is conditional probability.


