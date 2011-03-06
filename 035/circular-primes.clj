#!/usr/bin/env clj-env-dir
; The number, 197, is called a circular prime because all 
; rotations of the digits: 197, 971, and 719, are themselves 
; prime.
;
; There are thirteen such primes below 100: 
; 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
;
; How many circular primes are there below one million?

(ns circular-primes
  (:use clojure.string)
  (:use clojure.contrib.seq-utils))

(defn digits [number]
  ; convert the number to a string,
  ; and convert each char to an int.
  ;
  ; subtract 48 because casting a char
  ; to an int returns the ASCII
  ; representation of that char.
  (map #(- (int %) 48) (str number))) 

(defn divisors [n]
    "Returns a list of the proper divisors of n."
    (cons n (filter #(zero? (mod n %)) (range 1 (+ 1 (/ n 2))))))

(defn prime-factors-of [num]
  "Returns a sorted list of prime factors of num, including multiplicity."
  (let [q (Math/sqrt num)
        factor? (fn [nom den] (zero? (rem nom den)))]
    (loop [n num
           d 2
           r []]
      (cond
       (> d q) (concat r [n])
       (= n d) (concat r [n])
       (factor? n d) (recur (/ n d) d (conj r d))
       true          (recur n (inc d) r)))))

(defn num-divisors-fast [num]
    (let [freqs (reduce #(assoc %1 %2 (inc (get %1 %2 0)))
                                              {} (prime-factors-of num))]
          (reduce #(* %1 (inc %2)) 1 (vals freqs))))
(defn prime? [n]
  (and 
    (not (or (= n 1) (= n 0)))
    (= (num-divisors-fast n) 2)))

(defn circular-prime? [n]
  (every? prime? (map #(Integer/parseInt (join %)) (rotations (digits n)))))

(time (println (count (filter circular-prime? (range 1000000)))))
