# coding:utf-8
import json

filename = 'aj.json'
with open(filename) as f:
    aj = json.load(f)
    data=aj['data']
    
    for jl in data:
        job_type=jl['job_type']
        recruitment_company=jl['recruitment_company']['slug']
        id=jl['id']
        title=jl['title']
        company_name=jl['company_name']
        city=jl['city']
        country=jl['country']
        hash_id=jl['hash_id']
        thumb_url=jl['thumb_url']
        location_formatted=jl['location_formatted']
        work_remotely=jl['work_remotely']
        offer_relocation=jl['offer_relocation']
        
        #print(job_type+" "+recruitment_company+" "+str(id)+" "+title+" "+company_name+" "+city+" "+country+" "+hash_id+" "+thumb_url+" "+location_formatted+" "+str(work_remotely)+" "+str(offer_relocation))
        #print company_name
        print "https://www.artstation.com/jobs/"+hash_id 
