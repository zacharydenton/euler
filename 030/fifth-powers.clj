#!/usr/bin/env clojure
(defn ** [x n]
  (. (. java.math.BigInteger (valueOf x)) (pow n)))

(defn digits [number]
  ; convert the number to a string,
  ; and convert each char to an int.
  ;
  ; subtract 48 because casting a char
  ; to an int returns the ASCII
  ; representation of that char.
  (map #(- (int %) 48) (str number))) 

(defn can-be-written-as-sum-of-fifths? [number]
  ; if the sum of the digits raised to
  ; themselves is equal to the number 
  ; itself, then it is a munchausen number.
  (and (not (= number 1)) (= (apply + (map #(** % 5) (digits number))) number)))

(println (reduce + (filter can-be-written-as-sum-of-fifths? (range 500000))))
