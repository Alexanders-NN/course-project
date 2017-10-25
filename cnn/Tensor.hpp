#pragma once
#include <iostream>
#include <vector>

template<typename T>
class Tensor
{
	using value_type = std::vector<std::vector<T>>;
	using size_type = size_t;

	size_type Width;
	size_type Heigth;
	size_type Depth;
	std::vector<value_type> Matrix;

public:
	Tensor();

	Tensor(std::vector<value_type> pix);

	~Tensor();

	Tensor& convolution(const Tensor& matrix);

	size_type getMatrix() const;

	Tensor& operator *=(const Tensor&);

	T ReLU(T value);
};