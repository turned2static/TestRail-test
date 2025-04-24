from testrail import *
from getpass import *

#web_address = input('Enter your testrail address: ')
client = APIClient('https://fyodortraining.testrail.io/')
#client = APIClient('https://fyodortraining.testrail.io/')
client.user = 'fyodor.repollo@gurock.io'
client.password = ''
#client.password = getpass('Password: ')
'''
def add_result(self, test_ids, status, comment='', defects=None, duration=0):
        """
        Add a new result to results dict to be submitted at the end.

        :param defects: Add defects to test result
        :param list test_ids: list of test_ids.
        :param int status: status code of test (pass or fail).
        :param comment: None or a failure representation.
        :param duration: Time it took to run just the test.
        """
        for test_id in test_ids:
            data = {
                    'case_id': test_id,
                    'status_id': status,
                    'comment': comment,
                    'duration': duration,
                    'defects': defects
                }
            self.results.append(data)
            '''

update_result = client.send_post('add_result/24854',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24855',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24856',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24857',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24858',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24859',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24860',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24861',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24862',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24863',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24864',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24865',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24866',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24867',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24868',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24869',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24870',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24871',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24872',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24873',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24874',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24875',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24876',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24877',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24878',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24879',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24880',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24881',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24882',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24883',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24884',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24885',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24886',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24887',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24888',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24889',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24890',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24891',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24892',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24893',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24894',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24895',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24896',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24897',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24898',{"status_id": 1,"comment": "This test passed"})
update_result = client.send_post('add_result/24899',{"status_id": 1,"comment": "This test passed"})

print(update_result)
