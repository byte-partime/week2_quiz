# Week 2 quiz

* write a function that checks if two binary trees are the same

* ie. you could check if each node and its left and right child are identical for both trees

```

	    1			
	   / \
	  2   3   
	  			both of these trees are the same
	    1
	   / \
	  2   3
```

```
	    1			
	     \
	      2   
	  			both of these trees are not the same
	    1
	   / 
	  2   
```

```
	    1			
	   / \
	  3   2   
	   			both of these trees are not the same
	    1
	   / \
	  2   3
```

```
	    1			
	   / \
	  2   3
	   \
	    4   
	  			both of these trees are not the same
	    1
	   / \
	  2   3
	       \
	        4
	 
```