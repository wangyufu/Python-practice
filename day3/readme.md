sql
==
---
##�л���staff_table����Ŀ¼��    
���Զ��ļ�����select��delete��update��insert������##
---

1��select
=
**SELECT ������ FROM ������ WHERE �� ����� ֵ**        
**WHERE�Ӿ��ǿ�ѡ��**    

���磺
python sql.py select * from staff_table   
python sql.py select * from staff_table where age ">" 22   
python sql.py select name,age from staff_table where age ">" 22   

*��������ֶ����벻��ȷ����ʾ����������ȷ�ֶ�*    
*��������ֶ�������ȷ����ӡ���ϲ�ѯ���������벢������*    
*����Ϊstaff_id, name, age, phone, dept, enroll_date*    
*������Ϊ�̶�staff_table*    
*�����Ϊ">"|"="|"<"|"like"*    
*��Ϊ��>����<����=����Windows���ѱ����壬���Բ���ֱ��ʹ����Ҫ������*    

---
2��update
=
**UPDATE ������ SET �� = ֵ  WHERE �� ����� ֵ**    
**WHERE�Ӿ��ǿ�ѡ��**

���磺
python sql.py update staff_table set dept "=" DT    
python sql.py update staff_table set dept "=" DT where age ">" 22    

*��������ֶ����벻��ȷ����ʾ����������ȷ�ֶ�*    
*��������ֶ�������ȷ���޸���ֵ���޸ĳɹ����ӡ��ʾ��û�޸���ʾ��ӡû��ƥ�������*     

---
3��delete
=
**DELETE FROM ������ WHERE �� = ֵ**    
**WHERE�Ӿ��Ǳ�ѡ��й̶�Ϊstaff_id**    

���磺
python sql.py delete from staff_table where staff_id "=" 4    

*��������ֶ����벻��ȷ����ʾ����������ȷ�ֶ�*    
*��������ֶ�������ȷ��ɾ���������ݣ�ɾ���ɹ����ӡ��ʾ��ûɾ���ɹ���ʾ��ӡû�д�������*    

---
4��insert
=
**INSERT INTO ������ VALUES ֵ1��ֵ2...**       

���磺    
python sql2.py insert into staff_table values name,age,phone,dept,enroll_date    
   
*staff_id������룬staff_id����*   
*��������ֶ����벻��ȷ����ʾ����������ȷ�ֶ�*    
*��������ֶ�������ȷ�������������ݣ�����ɹ����ӡ��ʾ��phone��Ψһʱ��ʾphone�ظ�*   