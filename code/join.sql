with solo as (SELECT * from idols
WHERE group_name is NULL)

select * from mvs
inner join solo on mvs.artist=solo.stage_name

select * from mvs
inner join boy_groups on mvs.artist=boy_groups.name

select * from mvs
inner join girl_groups on mvs.artist=girl_groups.name