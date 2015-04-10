# jank jank jank
pages= ["About ", "Who We Are", "Volunteers", "Honors", "Events", "Reshaping Rochester", "Charrettes", "Exhibits", "Annual Awards", "Our Work", "Projects and Services", "Programs", "Results", "Resources", "Vision Plans", "Listen", "News", "Press", "Newsletter", "Grant Program", "About", "Apply", "Funded Projects", "Consultants", "FAQ", "Donate"]


for p in pages:

  slug = p.strip().lower().replace(" ", "-") + ".md"
  print """echo Title: """ + p + """     >  """ + slug
  
  print "echo  '' >> " + slug
  print "echo  '' >> " + slug
  print "echo  '' >> " + slug
  print "echo " + p + " >> "  + slug
  print "echo " + "".join(["=" for i in range(0, len(p))]) + " >> " + slug
