GEN = ENV["GEN_EXE"]
SOL = ENV["SOL_EXE"]

for i = 1:10
    # filename 0001.in, 0002.in and so on
    testname = string(i,base=10,pad=3)
    
    open(f->write(f, read(`$GEN $i`, String)), "$(testname).in", "w")
    open(f->write(f, read(pipeline(`cat $(testname).in`,`$SOL`), String)), "$(testname).ans", "w")
end

