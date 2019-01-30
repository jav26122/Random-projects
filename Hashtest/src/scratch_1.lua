-- 32-126

function toByte(s, offset)
    r = 0
    if offset == true then
        r = string.byte(s) - 32
    else
        r = string.byte(s)
    end
    return r

end

function toBits(s, offset)
    b = ""
    l = string.len(s)
    for i=1, l do
        if offset == true then
            ascii = toByte(string.sub(s, l - i + 1, l - i + 1), true)
        else
            ascii = toByte(string.sub(s, l - i + 1, l - i + 1))
        end
        q = ascii
        while q > 0 do
            if q % 2 == 1 then
                b = "1"..b
            else
                b = "0"..b
            end
            q = math.floor(q/2)
        end
        b = " "..b
    end
    return b
end

function flip(b)
    s = ""
    for i=1, string.len(b) do
        s = string.sub(b, i, i)..s
    end
    return s
end

function median(t) -- table input
    r = 0
    if #t > 0 then
        if #t%2 == 0 then -- even entries
            r = (string.byte( t[math.floor(#t/2)] ) + string.byte( t[math.floor(#t / 2 + 1)]) ) / 2
        else
            r = string.byte( t[math.ceil(#t/2)] )
        end
    end
    return r
end


function tablechars(s)
    t={}
    for i=1, string.len(s) do
        table.insert(t, string.sub(s, i, i))
    end
    return t
end

function byteAvg(s)
    a=0
    for i=1, string.len(s) do
        a = (a + string.byte(s)) / (i + 1)
    end
    return a
end

function hash(seed, Bytes)
    sl = string.len(seed)
    div = Bytes / sl
    track = 1
    newh = string.sub(seed, sl%div, sl%div)
    for i=1, Bytes do
        if track > sl - 1 then
            track = 1
        else
            track = track + 1
        end
        tc = tablechars(newh)
        h1 = math.floor(median(tc)) - byteAvg(newh) / 4
        if track == 1 then
            h2 = string.byte(string.sub(seed, track + 1, track + 1))
        else
            h2 = string.byte(string.sub(seed, track - 1, track - 1)) + (byteAvg(newh) / 2 + byteAvg(seed) / 2) / 2
        end
        if string.len(newh) == 0 then
            h = (h1+h2) / 2
        else
            hhh = string.sub(newh, string.len(newh), string.len(newh))
            h = (h1+h2)/2 + string.byte(hhh) / 6
        end

        if h > 126 then
            h = h - math.floor(h/track)
            if h < 32 then
                h = h + math.floor(h/2)
            end
        end
        newh = newh..string.char(h)
    end
    print(newh)
    return newh
end

while true do

    hash(io.read(), 128)
end