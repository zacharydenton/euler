#!/usr/bin/env clojure
; The series, 
; 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.
;
;Find the last ten digits of the series, 
;1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).

(defn ** [x n]
  (. (. java.math.BigInteger (valueOf x)) (pow n)))

(defn raise-to-itself [number]
  (** number number))

(println (reduce + (map raise-to-itself (range 1 1001))))
