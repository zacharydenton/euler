import qualified Data.Set as Set

triangles :: [Int]
triangles = [(n*(n + 1)) `quot` 2 | n <- [1..]]

pentagonals :: [Int]
pentagonals = [(n*(3*n - 1)) `quot` 2 | n <- [1..100000]]

hexagonals :: [Int]
hexagonals = [n*(2*n - 1) | n <- [1..100000]]

candidates :: [Int]
candidates = dropWhile (<= 40755) [t | t <- triangles, isPentagonal t, isHexagonal t]
    where isPentagonal = (`Set.member` Set.fromList pentagonals)
          isHexagonal = (`Set.member` Set.fromList hexagonals)

main :: IO ()
main = print $ head candidates
