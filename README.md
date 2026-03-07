### Readme Update
**Date: February 18, 2026**

#### Accomplishments

  * **Move Indexing Logic:** Established a process to find the correct index (`J`) of the move within the 2D probability array (`Prob`) since the move position does not always correspond directly to the index.
  * **Probability Update:** Developed conditional logic to increase the move's probability by 5% (`* 1.05`) if the player who made the move was the winner, and decrease it by 5% (`* 0.95`) if the player was the loser.
  * **Normalization Function:** Created a new `normalize` function to ensure all probabilities in the array sum up to 1 (100%).
  * **Rounding and Error Correction:** Implemented rounding of probabilities to three decimal places and added logic to account for any residual probability due to rounding errors by adjusting the last element of the array.

#### Next Steps

  * **File Update:** Implement the logic to overwrite the corresponding line in the file with the newly calculated and normalized probability array.
  * **Recursion Check:** T W noted the importance of adding a check to the recursive call within the `normalize` function to prevent it from potentially falling into an infinite loop, specifically when the normalization causes the last element's probability to become negative.
