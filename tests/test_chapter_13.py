#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_tester import ChapterTest

class Chapter13Test(ChapterTest):
    chapter_name = 'chapter_13'
    previous_chapter = 'chapter_12'

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(self.listings[1].type, 'test')
        self.assertEqual(self.listings[2].type, 'output')

        # prep
        self.sourcetree.start_with_checkout(self.previous_chapter)
        self.prep_database()

        # skips
        self.skip_with_check(37, '# should show changes') # diff

        # hack fast-forward
        skip = False
        if skip:
            self.pos = 28
            self.sourcetree.run_command('git checkout {}'.format(
                self.sourcetree.get_commit_spec('ch12l011')
            ))


        while self.pos < len(self.listings):
            print(self.pos, self.listings[self.pos].type)
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(ignore=["Generated by Django 1.10"])


if __name__ == '__main__':
    unittest.main()
