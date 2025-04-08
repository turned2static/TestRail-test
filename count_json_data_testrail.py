import json

null = None
false = False
json_data = json.dumps({
	"cases": [
		{
			"id": 17569,
			"title": "Existent test",
			"section_id": 2940,
			"template_id": 2,
			"type_id": 7,
			"priority_id": 2,
			"milestone_id": null,
			"refs": null,
			"created_by": 1,
			"created_on": 1667922004,
			"updated_by": 1,
			"updated_on": 1667922004,
			"estimate": null,
			"estimate_forecast": null,
			"suite_id": 174,
			"display_order": 1,
			"is_deleted": 0,
			"case_assignedto_id": null,
			"custom_automation_type": null,
			"custom_core": false,
			"custom_custom_elapsed": null,
			"custom_automation_id": "IdSoftware.Existent test",
			"custom_cust_comments": null,
			"custom_cust_status": null,
			"custom_preconds": null,
			"custom_steps": null,
			"custom_expected": null,
			"custom_steps_separated": null,
			"custom_mission": null,
			"custom_goals": null,
			"comments": []
		},
		{
			"id": 17570,
			"title": "Retrieve UUID across requests",
			"section_id": 2940,
			"template_id": 2,
			"type_id": 7,
			"priority_id": 2,
			"milestone_id": null,
			"refs": null,
			"created_by": 1,
			"created_on": 1667922005,
			"updated_by": 1,
			"updated_on": 1667922005,
			"estimate": null,
			"estimate_forecast": null,
			"suite_id": 174,
			"display_order": 2,
			"is_deleted": 0,
			"case_assignedto_id": null,
			"custom_automation_type": null,
			"custom_core": false,
			"custom_custom_elapsed": null,
			"custom_automation_id": "IdSoftware.Retrieve UUID across requests",
			"custom_cust_comments": null,
			"custom_cust_status": null,
			"custom_preconds": null,
			"custom_steps": null,
			"custom_expected": null,
			"custom_steps_separated": null,
			"custom_mission": null,
			"custom_goals": null,
			"comments": []
		}
	]
})


item_dict = json.loads(json_data)
print(len(item_dict['cases']))