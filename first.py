import survey
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
print ("difference in days (first - others)", (first_avg - other_avg)* 7.0)
