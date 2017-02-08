sql
==
---
##切换到staff_table所在目录；    
可以对文件进行select、delete、update、insert操作；##
---

1、select
=
**SELECT 列名称 FROM 表名称 WHERE 列 运算符 值**        
**WHERE子句是可选项**    

例如：
python sql.py select * from staff_table   
python sql.py select * from staff_table where age ">" 22   
python sql.py select name,age from staff_table where age ">" 22   

*如果命令字段输入不正确将提示，请输入正确字段*    
*如果命令字段输入正确将打印符合查询条件的输入并共几行*    
*列名为staff_id, name, age, phone, dept, enroll_date*    
*表名称为固定staff_table*    
*运算符为">"|"="|"<"|"like"*    
*因为“>”“<”“=”在Windows中已被定义，所以不能直接使用需要加引号*    

---
2、update
=
**UPDATE 表名称 SET 列 = 值  WHERE 列 运算符 值**    
**WHERE子句是可选项**

例如：
python sql.py update staff_table set dept "=" DT    
python sql.py update staff_table set dept "=" DT where age ">" 22    

*如果命令字段输入不正确将提示，请输入正确字段*    
*如果命令字段输入正确将修改列值，修改成功后打印提示，没修改提示打印没有匹配的数据*     

---
3、delete
=
**DELETE FROM 表名称 WHERE 列 = 值**    
**WHERE子句是必选项，列固定为staff_id**    

例如：
python sql.py delete from staff_table where staff_id "=" 4    

*如果命令字段输入不正确将提示，请输入正确字段*    
*如果命令字段输入正确将删除这行数据，删除成功后打印提示，没删除成功提示打印没有此条数据*    

---
4、insert
=
**INSERT INTO 表名称 VALUES 值1，值2...**       

例如：    
python sql2.py insert into staff_table values name,age,phone,dept,enroll_date    
   
*staff_id无需键入，staff_id自增*   
*如果命令字段输入不正确将提示，请输入正确字段*    
*如果命令字段输入正确将插入这行数据，插入成功后打印提示，phone不唯一时提示phone重复*   