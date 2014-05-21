The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

$$
\begin{align}
1! + 4! + 5! = 1 + 24 + 120 = 145
\end{align}
$$

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three
such loops that exist:

$$
\begin{align}
169 &\to 363601 \to 1454 \to 169 \\
871 &\to 45361 \to 871 \\
872 &\to 45362 \to 872
\end{align}
$$

It is not difficult to prove that EVERY starting number will eventually
get stuck in a loop. For example,

$$
\begin{align}
69 &\to 363600 \to 1454 \to 169 \to 363601 \, (\to 1454) \\
78 &\to 45360 \to 871 \to 45361 \, (\to 871) \\
540 &\to 145 \, (\to 145)
\end{align}
$$

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million is
sixty terms.

How many chains, with a starting number below one million, contain
exactly sixty non-repeating terms?

