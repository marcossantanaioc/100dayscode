Cb=[[0.001,
  7.557543577091797e-06,
  1656.90]]

threshold_Cb=10.0


for inner_list in Cb:
    for index, element in enumerate(inner_list):
        if element > threshold_Cb:
            inner_list[index] = threshold_Cb


print(Cb)

[]