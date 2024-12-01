module Max3 where
max3 :: Int -> Int -> Int -> Int
{- max3 (a,b,c) mengirimkan nilai yang paling besar di antara a, b, dan c. Asumsi: a, b, c bilangan berbeda -}
max3 a b c
 | (a < b && b < c) || (b < a && a < c) = c
 | (c < a && a < b) || (a < c && c < b) = b
 | otherwise = a