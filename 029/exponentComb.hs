import Data.List (nub)

main ::  IO ()
main = print $ length $ nub [a^n | a <- [2..100], n <- [2..100]]
