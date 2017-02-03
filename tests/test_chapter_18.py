#!/usr/bin/env python3
import unittest

from book_tester import ChapterTest


class Chapter18Test(ChapterTest):
    chapter_name = 'chapter_18'
    previous_chapter = 'chapter_17'

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing')
        self.assertEqual(self.listings[1].type, 'other command')
        self.assertEqual(self.listings[2].type, 'output')

        # skips
        #self.skip_with_check(22, 'switch back to master') # comment

        # prep
        self.sourcetree.start_with_checkout(self.previous_chapter)
        self.prep_database()
        self.sourcetree.run_command('rm accounts/tests.py')

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 10
            self.sourcetree.run_command('git checkout {0}'.format(
                self.sourcetree.get_commit_spec('ch17l004')
            ))

        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)

        # tidy up any .origs from patches
        self.sourcetree.run_command('find . -name \*.orig -exec rm {} \;')
        self.sourcetree.run_command('git add . && git commit -m"final commit ch17"')
        self.check_final_diff(ignore=["moves"])


if __name__ == '__main__':
    unittest.main()
