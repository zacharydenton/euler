import Data.List (sort)
import qualified Data.Map as Map

cubes :: Map.Map String [Integer]
cubes = Map.fromListWith (++) [(sort (show cube), [cube]) | x <- [1..10000], let cube = x^3]

main :: IO ()
main = print $ minimum [minimum ns | (_, ns) <- Map.toList cubes, length ns == 5]
