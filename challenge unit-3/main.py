
def linearSearchProduct(ProductList, targetProduct):
  indices = []

  for index, product in enumerate(ProductList):
   if product == targetProduct:
    indices.append(index)

  return indices


# Example usage:
Products = ["shoes", "boot", "loafer", "shoes", "sandle", "shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct (Products, target)
print(result)