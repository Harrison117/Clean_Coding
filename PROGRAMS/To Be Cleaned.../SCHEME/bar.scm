
;	DOT MULTIPLICATION
;		Given two lists of EQUAL NUMBER OF ELEMENTS, get the summation of the
;			products of a pair of index n numbers from the two lists
;

	;(define (dotMul list1 list2)
	;	(if (not (= (length list1) (length list2)))
	;		#f
	;		(if (= (length list1) 1)
	;			(* (car list1) (car list2))
	;			(+ (* (car list1) (car list2)) (dotMul (cdr list1) (cdr list2)) )
	;		)
	;	)
	;)

(define (dotMultiplicationTail list1 list2 summation)
	(if (not (= (length list1) (length list2)))
		#f
		(if (= (length list1) 0)
			summation
			(dotMultiplicationTail (cdr list1) (cdr list2) (+ summation (* (car list1) (car list2)) ) )
		)
	)
)

(define (dotMul l1 l2) (dotMultiplicationTail l1 l2 0))


(define (buildMatrixResult matrix1 matrix2 matrixResult)
	(if (equal? matrix1 '())
		matrixResult
		(buildMatrixResult (cdr matrix1) matrix2 (append matrixResult (list(buildRowResult (car matrix1) matrix2 '())) ) )
	)
)

(define (buildRowResult listOfMatrix1 matrix2 listResult)
	(if (equal? matrix2 '())
		listResult
		(buildRowResult listOfMatrix1 (cdr matrix2) (append listResult (list(dotMul listOfMatrix1 (car matrix2) )) ) )
	)
)

; USED TO TRANSFER THE FIRST INDUVIDUAL ELEMENTS FROM DIFFERENT SUBLIST ROWS INTO ONE LIST
(define (transferFirstElementToNewList listSource listDestination)
	(if (equal? listSource '())
		listDestination
		(transferFirstElementToNewList (cdr listSource) (append listDestination (list(car(car listSource)))) )
	)
)

; USED TO TRANSFER THE REST OF THE SUBLIST ROWS (EXCLUDING THE FIRST ELEMENT) INTO A NEW TEMPORARY MATRIX
(define (transferRestToNewMatrix listSource listDestination)
	(if (equal? listSource '())
		listDestination
		(transferRestToNewMatrix (cdr listSource) (append listDestination (list (cdr (car listSource))) ) )
	)
)

; REARRANGE THE MATRIX IN A WAY ITERATION AND DOT MULTIPLICATION IS POSSIBLE
(define (rearrangeSecondMatrix matrix2 newMatrix)
	; at the end of (transferRestToNewMatrix matrix2 '()), it would return (() () ...)
	;
	(if (equal? (car matrix2) '())
		newMatrix
		(rearrangeSecondMatrix (transferRestToNewMatrix matrix2 '()) (append newMatrix (list(transferFirstElementToNewList matrix2 '())) ) )
	)
)

(define g
	'(
		(1 2 3)
		(4 5 6)
		(7 8 9)
	)
)
(define h
	'(
		(1 4 7)
		(2 5 8)
		(3 6 9)
	)
)

(buildMatrixResult g (rearrangeSecondMatrix h '()) '())
