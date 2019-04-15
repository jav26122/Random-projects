
-- This program attemps to find a relationship between two given inputs of numbers in the hopes of finding a way to mathematically convert between them without already knowing what that relationship is.
-- Version Beta


Input = {2}
Output = {0.5}

functs = { o1 = "'n' root", o2 = "'n' Square", o3 = "Inverse", o4 = "Opposite", o5 = "'n' difference", o6 = "'n' multiple", o7 = "'n' divisor"};

function tlength(t)
  local c = 0;
  for _ in pairs(t) do c = c + 1 end
  return c;
end



function relation(n, input, output, functions)
  local tc = tlength(functions)
  for i=1, tc do
    for j=1, tc do
      if j == 1 then -- n root
        for k=1, n do
          newOut = math.pow(input[i], 1/k)
          if newOut == output[i] then
            return i, n
          end
        end
      elseif j == 2 then
        for k=1, n do
          newOut = math.pow(input[i], k)
          if newOut == output[i] then
            return i, n
          end
        end
      elseif j == 3 then
        if output[i] == 1 / input[i] then
          return i
        end
      elseif j == 4 then
        if output[i] == input[i] * -1 then
          return i
        end
      elseif j == 5 then
        for k=1, n * 2 do
          if k % 2 == 0 then
            if output[i] == input[i] - n then
              return i, n, k%2
            end
          elseif output[i] == input[i] + 1 then
            return i, n, k%2
          end
        end
      elseif k == 6 then
        for k=1, n do
          newOut = input[i] * n
          if output[i] == newOut then
            return i, n
          end
        end
      elseif k == 7 then
        for k=1, n do
          newOut = input[i] / n
          if output[i] == newOut then
            return i, n
          end
        end
      end
    end

  end
end



print(relation(10, Input, Output, functs))




print("Program ran sucessfully.")
while true do end
