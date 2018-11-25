select Userid, sum(case when Class = '文件' then 1 else 0) wenjian_no,
				sum(case when Class = '娱乐' then 1 else 0) yule_no，
				sum(case when Class = '食品' then 1 else 0) shipin_no，

from table where to_char(Consign_day,'yyyymm')='201804' v  
group by Userid;