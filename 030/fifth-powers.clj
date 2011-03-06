#!/usr/bin/env clojure
; Surprisingly there are only three numbers that can be 
; written as the sum of fourth powers of their digits:
;
; 1634 = 14 + 64 + 34 + 44
; 8208 = 84 + 24 + 04 + 84
; 9474 = 94 + 44 + 74 + 44
; As 1 = 14 is not a sum it is not included.
;
; The sum of these numbers is 1634 + 8208 + 9474 = 19316.
;
; Find the sum of all the numbers that can be written as 
; the sum of fifth powers of their digits.

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

;(def fifths (filter can-be-written-as-sum-of-fifths? (range 5000)))
;(println fifths)
(time (println (reduce + (filter can-be-written-as-sum-of-fifths? (range 500000)))))
