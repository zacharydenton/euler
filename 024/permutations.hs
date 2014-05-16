import Data.List (sort, permutations)

main :: IO ()
main = putStrLn $ (sort $ permutations ['0'..'9']) !! 999999
