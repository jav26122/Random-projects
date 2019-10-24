--[[
map = {}
math.randomseed(os.time())

function generateSubs(bits)
    local numBits = math.pow(2, bits)
    for i=1, numBits do
        repeat
            local unique = true
            local rand = math.random(1, numBits)
            for j=1, #map do
                if map[j][2] == rand then
                    unique = false
                end
            end
        until unique == true
        local tab = {i, rand}
        table.insert(map, tab)
    end
end

generateSubs(8)

for i=1, #map do
    io.write(map[i][2]..",")
end
]]

-- Random sub map that was generated using above code.
map = {6,67,43,63,17,149,42,97,93,131,83,247,188,9,191,4,185,84,2,256,215,156,186,198,234,180,251,53,89,135,196,104,200,38,243,60,165,29,163,184,177,95,225,102,151,182,239,219,116,181,190,242,91,161,136,14,34,115,235,69,221,232,252,141,214,103,59,173,122,30,82,171,168,100,55,204,192,45,201,209,138,208,140,23,240,86,56,99,154,226,37,57,172,160,155,133,246,118,62,205,20,65,121,46,21,10,223,137,18,119,245,220,73,74,231,130,128,253,75,105,224,3,31,85,107,80,179,145,47,159,197,39,194,8,41,71,24,218,202,129,178,58,127,19,92,230,176,193,13,33,250,114,120,61,143,213,25,157,32,164,244,108,27,207,206,189,175,125,68,66,76,26,254,255,109,212,132,64,222,144,106,169,79,139,44,134,236,147,210,111,153,98,233,101,167,110,12,5,96,94,211,142,72,11,36,187,199,49,50,228,229,162,126,117,248,22,35,51,113,88,81,52,87,216,152,150,237,1,124,195,54,203,170,146,158,77,238,78,183,227,148,217,166,48,7,123,40,241,249,70,15,174,28,90,112,16}
block = {15,77,86,57,56,205,55,106,76,71,168,118,10,93,167,67,184,208,160,234,100,241,206,196,92,60,240,115,188,231,82,202,73,104,207,9,99,181,174,74,97,94,5,137,22,31,148,52,192,32,162,62,242,194,133,225,201,112,144,221,177,68,36,224,158,253,79,211,21,145,186,187,13,249,173,105,38,37,11,193,64,24,244,147,117,228,143,136,255,127,251,199,132,198,163,39,70,26,17,65,165,129,175,43,46,111,154,110,18,238,256,130,109,122,235,195,171,89,54,237,14,213,98,95,28,189,170,215,19,169,209,7,78,114,85,134,108,47,87,236,222,219,107,172,125,80,151,96,124,140,146,16,176,141,150,190,91,179,131,252,53,254,218,135,204,183,119,155,245,61,246,29,102,40,58,164,250,178,1,35,182,66,243,156,223,101,230,30,59,227,20,217,88,220,83,191,42,161,2,142,239,75,49,103,226,120,185,216,200,45,121,157,50,128,90,44,84,180,41,139,153,51,210,25,247,214,116,72,23,126,113,81,8,248,232,203,6,12,33,212,63,197,149,34,138,166,27,152,4,233,3,48,123,69,159,229}
-- random block pairing generated.

b64 = {}
for i=65, 90 do
    table.insert(b64, string.char(i))
end
for i=97, 122 do
    table.insert(b64, string.char(i))
end
for i=48, 57 do
    table.insert(b64, string.char(i))
end
table.insert(b64, "+")
table.insert(b64, "/")


mask = 21473586

function toBinary(dec)
    local bits = {}
    while dec > 0 do
        r = math.fmod(dec, 2)
        bits[#bits + 1] = r
        dec = (dec - r) / 2
    end
    while #bits < 8 do
        table.insert(bits, 1, 0)
    end
    return table.concat(bits)
end

function toDecimal(bin)
    local bin = tostring(bin)
    bin = string.reverse(bin)
    local sum = 0
    for i=1, string.len(bin) do
        num = string.sub(bin, i, i) == "1" and 1 or 0
        sum = sum + num * math.pow(2, i-1)
    end
    return sum
end

key = "SomeMax32CharKey"
keyb = {}
for i=1, string.len(key) do
    sbyte = string.byte(string.sub(key, i, i))
    table.insert(keyb, toBinary(sbyte))
end
keyb = table.concat(keyb)


text = "some text to encrypt.."

function Round(s)
    result = {}
    len = string.len(s)
    for i=1, len do
        char = string.sub(s, i, i)
        charb = string.byte(char)
        newb = map[charb]
        table.insert(result, newb)
    end
    resultb = {}
    for i=1, #result do
        --print(toBinary(result[i])) -- byte char after substitution
        --print(string.char(result[i])) -- char
        table.insert(resultb, toBinary(result[i]))
    end
    newbits = {}
    for i=1, #resultb do
        bits = resultb[i] -- Should be 8 bits
        --print(bits)
        bitst = tostring(bits)
        --[[for j=1, string.len(bitst) do -- bitwise operations
            bitsnum = tonumber(string.sub(bitst, j, j)) -- 1 or 0
            --print("before"..bitsnum)
            --print("mask:"..tonumber(string.sub(tostring(mask), j, j)))
            maskb = tonumber(string.sub(tostring(mask), j, j))
            if maskb == 0 then
                maskb = nil
            end
            if bitsnum == 0 then
                bitsnum = nil
            end
            newbit = bitsnum and maskb
            if newbit == nil then
                newbit = 0
            end
            table.insert(newbits, newbit)
            print(newbit)
        end]]
        newbyte = {}
        for j=1, string.len(tostring(mask)) do
            masks = tostring(mask)
            newbit = string.sub(bitst, tonumber(string.sub(masks, j, j)), tonumber(string.sub(masks, j, j)))
            --print(newbit)
            table.insert(newbits, newbit)
        end
    end
    return table.concat(newbits)
end


function bitStreamToText(stream)
    streaml = string.len(stream)
    res = {}
    for i=0, streaml / 8 do
        section = string.sub(stream, i*8 + 1, i*8 + 8)
        --print(section)
        --print(toDecimal(section))
        --print(string.char(toDecimal(section)))
        table.insert(res, string.char(toDecimal(section)))
    end
    return table.concat(res)
end

function bitStreamToB64(stream)
    streaml = string.len(stream)
    res = {}
    for i=1, streaml / 4 do
        section = string.sub(stream, 4 * (i-1) + 1, 4 * (i-1) + 5)
        print(section)
        print(toDecimal(section))
        table.insert(res, b64[toDecimal(section)+1])
    end
    return table.concat(res)
end



r = Round(text)
print(r)
print(bitStreamToB64(r))



