class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        
        for cpdomain in cpdomains:
            subRes = cpdomain.split(" ")
            c = int(subRes[0])
            fullDomain = subRes[1]
            domains[fullDomain] += c
            for i, ch in enumerate(fullDomain):
                if ch == ".":
                    domains[fullDomain[i + 1:]] += c
            
        res = []
        for domainCount in domains.items():
            res.append(str(domainCount[1]) + " "+  domainCount[0])
        
        return res