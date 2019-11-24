;;;======================================================
;;;  Basic Shape Identification
;;;     Type of shapes :
;;;         1. Triangle
;;;             a. Acute Triangle v
;;;             b. Obtuse Triangle v
;;;             c. Right Triangle v
;;;             d. Isosceles Triangle v
;;;                 i.  Right Isosceles Triangle
;;;                 ii. Obtuse Isosceles Triangle
;;;                 iii.Acute Isosceles Triangle
;;;             e. Equilateral Triangle v
;;;         2. Irregular quadrilaterals
;;;             a. Parallelogram v
;;;                 i.  Rhombus
;;;                 ii. Kite
;;;             b. Trapezium
;;;                 i.  Isosceles Trapezium
;;;                 ii. Right Trapezium
;;;                 iii.Left Trapezium
;;;         3. Pentagon v
;;;         4. Hexagon v
;;;     
;;;
;;;======================================================


;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction ask-question (?question $?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer) 
       then (bind ?answer (lowcase ?answer)))
   (while (not (member ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer) 
          then (bind ?answer (lowcase ?answer))))
   ?answer)

(deffunction yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n))
   (if (or (eq ?response yes) (eq ?response y))
       then yes 
       else no))


;;*******************************
;;* CHOOSE SHAPE RULES *
;;*******************************

(defrule determine-which-geometric ""
   (not (number-of-vertices ?))
   (not (known ?))
   =>
   (assert (number-of-vertices (ask-question "How many vertices the shape has ?" three four five six )))
)
;;****************
;;* Triangle *
;;****************
(defrule type-of-triangles ""
   (number-of-vertices three)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the triangle has ?" two three none)))
)

(defrule type-of-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (not (known ?))
   =>
   (assert (angles-type (ask-question "What angle do the triangle has ?" acute obtuse right)))
)



(defrule type-of-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (not (known ?))
   =>
   (assert (number-acute-angles (ask-question "Number of acute angle(s) in triangle ?" two three )))
)

(defrule acute-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles three)
   (not (known ?))
   =>
   (assert (known " Acute Triangle"))
)

(defrule obtuse-or-right-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (not (known ?))
   =>
   (assert (number-right-angles (ask-question "Number of right angle in triangle ?" one none)))
)

(defrule right-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (number-right-angles one)
   (not (known ?))  
   =>
   (assert (known "Right triangle"))
)

(defrule obtuse-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (number-right-angles none)
   (not (known ?))  
   =>
   (assert (known "Obtuse triangle"))
)
(defrule acute-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type acute)
   =>
   (assert (known "Isosceles Acute Triangle"))
)
(defrule obtuse-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type obtuse)
   =>
   (assert (known "Isosceles Obtuse Triangle"))
) 

(defrule right-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type right)
   =>
   (assert (known "Isosceles Right Triangle"))
) 

(defrule equilateral-triangle ""
   (number-of-vertices three)
   (number-of-same-edges three)
   (not (known ?))  
   =>
   (assert (known "Equilateral triangle"))
)
;;****************
;;*  Quadrilaterals *
;;****************
(defrule type-of-quadrilaterals ""
   (number-of-vertices four)
   (not (known ?))
   =>
   (assert (all-same-edges  (yes-or-no-p "Are all the edges has equal length ")))
)

(defrule square-or-rhombus ""
   (number-of-vertices four)
   (all-same-edges yes)
   (not (known ?))
   =>
   (assert (is-the-angles-right (yes-or-no-p "Are all the angles are right angles")))
)
;;****************
;;* Square*
;;****************

(defrule square-shape""
   (number-of-vertices four)
   (all-same-edges yes)
   (is-the-angles-right yes)
   (not (known ?))
   =>
   (assert (known "Square"))
)

;;****************
;;* Rectangle*
;;****************

(defrule square-or-rectangle""
   (number-of-vertices four)
   (all-same-edges no)
   (not (known ?))
   =>
   (assert (is-the-angles-right (yes-or-no-p "Are all the angles are right angles")))
)
(defrule rectangle-shape""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right yes)
   (not (known ?))
   =>
   (assert (known "Rectangle"))
)
;;****************
;;* Rhombus*
;;****************

(defrule rhombus-shape""
   (number-of-vertices four)
   (all-same-edges yes)
   (is-the-angles-right no)
   (not (known ?))
   =>
   (assert (known "Rhombus"))
)
;;****************
;;* Parallelogram / Trapezium *
;;****************
(defrule type-of-parallelogram ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (not (known ?))
   =>
   (assert (number-of-parallel(ask-question "How many pair of parallel side does the quadrilateral have ? " two none)))
)

;;****************
;;* Parallelogram *
;;****************
(defrule parallelogram-or-kite ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (number-of-parallel two)
   (not (known ?))
   =>
   (assert (known "Parallelogram"))
)

(defrule kite-parallelogram ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (number-of-parallel none)
   (not (known ?))
   =>
   (assert (consecutive-sides-are-congruent(yes-or-no-p "Do the consecutive sides are congruent")))
)

(defrule kite-shape ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (number-of-parallel none)
   (consecutive-sides-are-congruent yes)
   (not (known ?))
   =>
   (assert (known "Kite"))
)

(defrule quadrilaterals-v2 ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (number-of-parallel none)
   (consecutive-sides-are-congruent no)
   (not (known ?))
   =>
   (assert (known "Irregular quadrilateral"))
)

(defrule quadrilaterals ""
   (number-of-vertices four)
   (all-same-edges no)
   (is-the-angles-right no)
   (number-of-parallel yes)
   (not (known ?))
   =>
   (assert (known "Irregular Trapezium"))
)
;;****************
;;* Trapezoid *
;;****************

(defrule type-of-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (not (known ?))
   =>
   (assert (is-the-legs-congruent (yes-or-no-p "Does the legs congruent ?")))
)

(defrule isosceles-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent yes)
   (not (known ?))
   =>
   (assert (known "Isosceles Trapezium"))
)

(defrule left-right-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (not (known ?))
   =>
   (assert (right-angle-position(ask-question "Where do the right angle locates ?" right left)))
)

(defrule right-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (right-angle-position right)
   (not (known ?))
   =>
   (assert (known "Right Trapezium"))
)

(defrule left-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (right-angle-position left)
   (not (known ?))
   =>
   (assert (known "Left Trapezium"))
)

;;****************
;;* Pentagon *
;;****************
(defrule is-pentagon ""
   (number-of-vertices five)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the pentagon has ?" five other)))
)
(defrule regular-pentagon-shape ""
   (number-of-vertices five)
   (number-of-same-edges five)
   (not (known ?))
   =>
   (assert (known "Regular Pentagon"))
)

(defrule irregular-pentagon-shape ""
   (number-of-vertices five)
   (number-of-same-edges other)
   (not (known ?))
   =>
   (assert (known "Irregular Pentagon"))
)

;;****************
;;* Hexagon *
;;****************
(defrule is-hexagon""
   (number-of-vertices six)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the hexagon has ?" six other)))
)
(defrule regular-hexagon-shape ""
   (number-of-vertices six)
   (number-of-same-edges six)
   (not (known ?))
   =>
   (assert (known "Regular Hexagon"))
)

(defrule irregular-hexagon-shape ""
   (number-of-vertices six)
   (number-of-same-edges other)
   (not (known ?))
   =>
   (assert (known "Irregular Hexagon"))
)



;;****************
;;* Print Result *
;;****************
(defrule print-result ""
  (declare (salience 10))
  (known ?item)
  =>
  (printout t "Shape:")
  (printout t crlf crlf)
  (format t " %s%n%n%n" ?item))
