import pytest
import fonctions as f

def test_1 ( ) :
	assert f . puissance (2 ,3) == 8
	assert f . puissance (2 ,2) == 4

def test_2 ( ) :
	assert f . puissance (2 ,3) == 8
	assert f . puissance (2 ,2) == 4

def test_limite ( ) :
	assert f . puissance (0.5 ,3) == 0.125
	assert f . puissance (3 ,0.5) == 1.732050808
	assert f . puissance (3 ,-0.5) == 0.5773502692
	assert f . puissance (1 ,1) == 1
	assert f . puissance (1 ,-1) == 1
	assert f . puissance (-1 ,1) == -1
	assert f . puissance (-1 ,-1) == -1
	assert f . puissance (0 ,-1) == 0
