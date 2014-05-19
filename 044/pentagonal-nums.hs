import qualified Data.Set as Set

pentagonals :: [Int]
pentagonals = [(n*(3*n - 1)) `quot` 2 | n <- [1..3000]]

isPentagonal :: Int -> Bool
isPentagonal n = Set.member n (Set.fromList pentagonals)

candidates :: [Int]
candidates = [j - k | j <- pentagonals, k <- takeWhile (< j) pentagonals,
                      isPentagonal (j - k), isPentagonal (j + k)]

main :: IO ()
main = print $ head candidates
