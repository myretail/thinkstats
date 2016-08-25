import survey
import thinkstats
import sys, math
table = survey.Pregnancies()
table.ReadRecords()
print ('Number of pregnancies', len(table.records))

first_p=[record for record in table.records if record.outcome==1 and record.birthord==1]
other_p=[record for record in table.records if record.outcome==1 and record.birthord>1]

def avg_prg_lenth(records):
    s= sum([record.prglength for record in records])
    return float(s)/len(records)

first_avg = avg_prg_lenth(first_p)
other_avg = avg_prg_lenth(other_p)

print ("Live, first births", len(first_p), "%s" % first_avg)
print ("Live, not first births", len(other_p), "%s" % other_avg)
print ("difference in hours (first - others)", (first_avg - other_avg)* 7.0 *24.0)

pregnancyFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord == 1]
pregnancyNonFirst = [rec.prglength for rec in table.records if rec.outcome == 1 and rec.birthord > 1]

print ("一胎标准差： ",math.sqrt(thinkstats.Var(pregnancyFirst)))
print ("其他标准差： ",math.sqrt(thinkstats.Var(pregnancyNonFirst)))

sdDiff = abs(math.sqrt(thinkstats.Var(pregnancyFirst))-math.sqrt(thinkstats.Var(pregnancyNonFirst)))
print ("SD gestation time diff", sdDiff, "weeks", sdDiff * 7, "days", sdDiff * 7 * 24, "hours")
