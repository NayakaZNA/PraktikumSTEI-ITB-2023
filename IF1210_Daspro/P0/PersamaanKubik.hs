module PersamaanKubik where
 persamaanKubik :: Int -> Int -> Int -> Int -> Int -> Bool
 persamaanKubik a b c d x = a*x^3 + b*x^2 + c*x + d == 0