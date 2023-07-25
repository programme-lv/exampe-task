GEN = ENV["GEN_EXE"]

for i = 1:10
    # filename 0001.in, 0002.in and so on
    testname = string(i,base=10,pad=3)
    filename = "$(testname).in"
    open(f->write(f, read(`$GEN $i`, String)), filename, "w")
end

