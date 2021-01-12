# coding = 'utf-8'
import numpy as np
import pandas as pd
from line_profiler import LineProfiler

# @profile
def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result

# @profile
def target_mean_v2(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    value_dict = dict()
    count_dict = dict()
    for i in range(data.shape[0]):
        if data.loc[i, x_name] not in value_dict.keys():
            value_dict[data.loc[i, x_name]] = data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] = 1
        else:
            value_dict[data.loc[i, x_name]] += data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] += 1
    for i in range(data.shape[0]):
        result[i] = (value_dict[data.loc[i, x_name]] - data.loc[i, y_name]) / (count_dict[data.loc[i, x_name]] - 1)
    return result

# @profile
def target_mean_v3(data:pd.DataFrame, y_name:str, x_name:str) -> np.ndarray:
  shape = data.shape[0]
  result = np.zeros(shape)
  value_dict = dict()
  count_dict = dict()

  for i in range(shape):
        loc_y = data.loc[i, y_name]
        loc_x = data.loc[i, x_name]
        if loc_x not in value_dict:
            value_dict[loc_x] = loc_y
            count_dict[loc_x] = 1
        else:
            value_dict[loc_x] += loc_y
            count_dict[loc_x] += 1
  for i in range(shape):
        loc_y = data.loc[i, y_name]
        loc_x = data.loc[i, x_name]
        result[i] = (value_dict[loc_x] - loc_y) / (count_dict[loc_x] - 1)
  return result

# @profile
def target_mean_v4(data:pd.DataFrame, y_name:str, x_name:str) -> np.ndarray:
  shape = data.shape[0]
  result = np.zeros(shape)
  value_dict = dict()
  count_dict = dict()

  loc_y_column = data.loc[:, y_name]
  loc_x_column = data.loc[:, x_name]

  for i in range(shape):
    loc_y = loc_y_column[i]
    loc_x = loc_x_column[i]
    if loc_x not in value_dict:
      value_dict[loc_x] = loc_y
      count_dict[loc_x] = 1
    else:
      value_dict[loc_x] += loc_y
      count_dict[loc_x] += 1
  for i in range(shape):
    loc_y = loc_y_column[i]
    loc_x = loc_x_column[i]
    result[i] = (value_dict[loc_x] - loc_y) / (count_dict[loc_x] - 1)
  return result

def target_mean_v5(data:pd.DataFrame, y_name:str, x_name:str) -> np.ndarray:
  shape = data.shape[0]
  result = np.zeros(shape)
  value_dict = dict()
  count_dict = dict()

  loc_y_column = data.loc[:, y_name].values
  loc_x_column = data.loc[:, x_name].values

  for i in range(shape):
    loc_y = loc_y_column[i]
    loc_x = loc_x_column[i]
    if loc_x not in value_dict:
      value_dict[loc_x] = loc_y
      count_dict[loc_x] = 1
    else:
      value_dict[loc_x] += loc_y
      count_dict[loc_x] += 1
  for i in range(shape):
    loc_y = loc_y_column[i]
    loc_x = loc_x_column[i]
    result[i] = (value_dict[loc_x] - loc_y) / (count_dict[loc_x] - 1)
  return result

def main():
    y = np.random.randint(2, size=(5000, 1))
    x = np.random.randint(10, size=(5000, 1))
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])

    # result_1 = target_mean_v1(data, 'y', 'x')
    # result_2 = target_mean_v2(data, 'y', 'x')
    # result_3 = target_mean_v3(data, 'y', 'x')
    #
    # diff = np.linalg.norm(result_1 - result_2)
    # print(diff)

    lp = LineProfiler()
    lp_wrapper = lp(target_mean_v5)
    lp_wrapper(data, 'y', 'x')
    lp.print_stats()


if __name__ == '__main__':
    main()
